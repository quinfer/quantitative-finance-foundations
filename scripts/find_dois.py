"""
Utility script to look up DOIs (and canonical URLs) for the core papers listed in
`papers/bibliography.csv` using the Crossref API, with a light human-in-the-loop
confirmation step.

USAGE (from repo root):

    python scripts/find_dois.py \
        --bib papers/bibliography.csv \
        --out papers/dois.csv

You will be shown 0–N candidate matches per paper and asked to confirm the correct DOI.
Confirmed mappings are written to the output CSV for later use (e.g. to enrich
`papers/essential-readings.md` with links).

NOTE:
- This script requires network access and the `requests` package.
- It is intentionally conservative: you confirm each DOI rather than accepting the
  top API result blindly.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from typing import List, Optional

import requests
from urllib.parse import urlencode


CROSSREF_API_URL = "https://api.crossref.org/works"


@dataclass
class Citation:
    key: str
    title: str
    authors: str
    year: Optional[int]
    journal: str


@dataclass
class Candidate:
    doi: str
    title: str
    year: Optional[int]
    journal: str


def load_bibliography(path: str) -> List[Citation]:
    citations: List[Citation] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = None
            if row.get("year"):
                try:
                    year = int(row["year"])
                except ValueError:
                    year = None
            citations.append(
                Citation(
                    key=row["key"].strip(),
                    title=row["title"].strip(),
                    authors=row.get("authors", "").strip(),
                    year=year,
                    journal=row.get("journal", "").strip(),
                )
            )
    return citations


def query_crossref(citation: Citation, rows: int = 5) -> List[Candidate]:
    """
    Query Crossref using a bibliographic string built from title and first author.
    Returns a small list of Candidate objects for manual review.
    """
    query = citation.title
    if citation.authors:
        # Use only first author to keep query robust
        first_author = citation.authors.split(";")[0]
        query += f" {first_author}"

    params = {
        "query.bibliographic": query,
        "rows": rows,
    }

    url = f"{CROSSREF_API_URL}?{urlencode(params)}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as exc:  # noqa: BLE001
        print(f"[WARN] Crossref request failed for {citation.key}: {exc}", file=sys.stderr)
        return []

    data = resp.json()
    items = data.get("message", {}).get("items", [])

    candidates: List[Candidate] = []
    for it in items:
        doi = it.get("DOI")
        if not doi:
            continue
        titles = it.get("title") or []
        title = titles[0] if titles else ""
        container_titles = it.get("container-title") or []
        journal = container_titles[0] if container_titles else ""
        year = None
        issued = it.get("issued", {})
        if "date-parts" in issued and issued["date-parts"]:
            year = issued["date-parts"][0][0]
        # Light year filter: keep near target year if provided
        if citation.year and year:
            if abs(citation.year - year) > 2:
                continue

        candidates.append(Candidate(doi=doi, title=title, year=year, journal=journal))

    return candidates


def prompt_user_choice(citation: Citation, candidates: List[Candidate]) -> Optional[Candidate]:
    """
    Print citation and candidate list; ask user to choose the correct one (or none).
    """
    print("\n" + "=" * 80)
    print(f"Key:      {citation.key}")
    print(f"Title:    {citation.title}")
    print(f"Authors:  {citation.authors}")
    print(f"Year:     {citation.year}")
    print(f"Journal:  {citation.journal}")
    print("-" * 80)

    if not candidates:
        print("No candidates returned by Crossref.")
        return None

    for idx, c in enumerate(candidates, start=1):
        print(f"{idx}. {c.title} ({c.journal}, {c.year})")
        print(f"   DOI: https://doi.org/{c.doi}")

    while True:
        choice = input("Select correct DOI [1–{0}, or 0 for none]: ".format(len(candidates))).strip()
        if choice.isdigit():
            i = int(choice)
            if 0 <= i <= len(candidates):
                if i == 0:
                    return None
                return candidates[i - 1]
        print("Invalid choice, please enter a number between 0 and {0}.".format(len(candidates)))


def write_dois(path: str, rows: List[dict]) -> None:
    fieldnames = ["key", "title", "authors", "year", "journal", "doi", "url"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Lookup DOIs for core bibliography via Crossref.")
    parser.add_argument("--bib", default="papers/bibliography.csv", help="Path to bibliography CSV.")
    parser.add_argument(
        "--out",
        default="papers/dois.csv",
        help="Output CSV path for confirmed DOIs and URLs.",
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=5,
        help="Maximum number of Crossref candidates to show per citation.",
    )
    args = parser.parse_args()

    citations = load_bibliography(args.bib)
    results: List[dict] = []

    print(f"Loaded {len(citations)} citations from {args.bib}")
    print("Querying Crossref (requires network access)...")

    for cit in citations:
        candidates = query_crossref(cit, rows=args.rows)
        chosen = prompt_user_choice(cit, candidates)
        if chosen is None:
            print(f"[INFO] Skipping DOI for {cit.key}")
            continue
        results.append(
            {
                "key": cit.key,
                "title": cit.title,
                "authors": cit.authors,
                "year": cit.year or "",
                "journal": cit.journal,
                "doi": chosen.doi,
                "url": f"https://doi.org/{chosen.doi}",
            }
        )

    write_dois(args.out, results)
    print(f"\nWritten {len(results)} confirmed DOIs to {args.out}")


if __name__ == "__main__":
    main()


