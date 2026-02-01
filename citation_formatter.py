# citation_formatter.py
"""
AMA Citation Formatter for PostopCare

Setup:
    No additional pip installs required

AMA Citation Format for Journal Articles:
    Authors. Article title. Journal Name Abbreviated. Year;Volume(Issue):Pages.
    
Examples:
    - Single author: Smith J. Article title. JAMA. 2023;330(1):45-52.
    - Multiple authors: Smith J, Johnson M, Williams K. Title. JAMA. 2023;330:45-52.
    - 6+ authors: Smith J, Johnson M, Williams K, et al. Title. JAMA. 2023;330:45-52.
"""

from typing import Optional


def format_citation(article: dict) -> str:
    """
    Format a single article in AMA citation style.
    
    Input (complete):
        article = {
            "authors": ["Smith J", "Johnson M", "Williams K"],
            "title": "Post-operative pain management in knee arthroplasty",
            "journal": "Journal of Bone and Joint Surgery",
            "year": 2023,
            "volume": "105",
            "issue": "4",
            "pages": "234-241",
            "pmid": "12345678"
        }
    
    Output:
        "Smith J, Johnson M, Williams K. Post-operative pain management in knee arthroplasty. J Bone Joint Surg. 2023;105(4):234-241."
    
    Input (many authors - use et al.):
        article = {
            "authors": ["Smith J", "Johnson M", "Williams K", "Brown R", "Davis T", "Wilson P", "Taylor M"],
            "title": "Large study on outcomes",
            "journal": "New England Journal of Medicine",
            "year": 2024,
            "volume": "390",
            "pages": "112-125"
        }
    
    Output:
        "Smith J, Johnson M, Williams K, et al. Large study on outcomes. N Engl J Med. 2024;390:112-125."
    
    Input (missing fields):
        article = {
            "authors": ["Smith J"],
            "title": "Brief report",
            "journal": "Surgery Today",
            "year": 2023
        }
    
    Output:
        "Smith J. Brief report. Surgery Today. 2023."
    """
    # TODO: Implement
    # 1. Format authors using format_authors()
    # 2. Get title (ensure it ends with period)
    # 3. Abbreviate journal name
    # 4. Build the citation string
    # 5. Handle missing fields gracefully
    #
    # parts = []
    # 
    # # Authors
    # authors_str = format_authors(article.get("authors", []))
    # if authors_str:
    #     parts.append(authors_str)
    #
    # # Title
    # title = article.get("title", "")
    # if title:
    #     if not title.endswith("."):
    #         title += "."
    #     parts.append(title)
    #
    # # Journal
    # journal = article.get("journal", "")
    # if journal:
    #     journal_abbr = abbreviate_journal(journal)
    #     parts.append(journal_abbr + ".")
    #
    # # Year, volume, issue, pages
    # year = article.get("year", "")
    # volume = article.get("volume", "")
    # issue = article.get("issue", "")
    # pages = article.get("pages", "")
    #
    # if year:
    #     year_part = str(year)
    #     if volume:
    #         year_part += f";{volume}"
    #         if issue:
    #             year_part += f"({issue})"
    #         if pages:
    #             year_part += f":{pages}"
    #     year_part += "."
    #     parts.append(year_part)
    #
    # return " ".join(parts)
    pass


def format_authors(authors: list[str]) -> str:
    """
    Format author list according to AMA style.
    
    AMA Rule: List up to 6 authors. If more than 6, list first 3 then "et al."
    
    Input:
        authors = ["Smith J", "Johnson M", "Williams K"]
    Output:
        "Smith J, Johnson M, Williams K."
    
    Input (more than 6 - use et al.):
        authors = ["Smith J", "Johnson M", "Williams K", "Brown R", "Davis T", "Wilson P", "Taylor M"]
    Output:
        "Smith J, Johnson M, Williams K, et al."
    
    Input (empty):
        authors = []
    Output:
        ""
    
    Input (single):
        authors = ["Smith J"]
    Output:
        "Smith J."
    """
    # TODO: Implement
    # if not authors:
    #     return ""
    #
    # if len(authors) > 6:
    #     # More than 6 authors: list first 3, then et al.
    #     return ", ".join(authors[:3]) + ", et al."
    # else:
    #     return ", ".join(authors) + "."
    pass


# Common journal abbreviations (expand as needed)
JOURNAL_ABBREVIATIONS = {
    "Journal of Bone and Joint Surgery": "J Bone Joint Surg",
    "New England Journal of Medicine": "N Engl J Med",
    "Journal of the American Medical Association": "JAMA",
    "JAMA": "JAMA",
    "Annals of Surgery": "Ann Surg",
    "British Medical Journal": "BMJ",
    "The Lancet": "Lancet",
    "Lancet": "Lancet",
    "Surgery": "Surgery",
    "Archives of Surgery": "Arch Surg",
    "American Journal of Surgery": "Am J Surg",
    "Journal of Surgical Research": "J Surg Res",
    "Orthopedics": "Orthopedics",
    "Clinical Orthopaedics and Related Research": "Clin Orthop Relat Res",
    "Journal of Arthroplasty": "J Arthroplasty",
    "Physical Therapy": "Phys Ther",
    "Pain Medicine": "Pain Med",
    "Anesthesiology": "Anesthesiology",
    "Obstetrics and Gynecology": "Obstet Gynecol",
    "American Journal of Obstetrics and Gynecology": "Am J Obstet Gynecol",
    "Journal of Trauma": "J Trauma",
    "Annals of Emergency Medicine": "Ann Emerg Med",
    "Emergency Medicine Journal": "Emerg Med J",
    "Spine": "Spine",
    "Journal of Neurosurgery": "J Neurosurg"
}


def abbreviate_journal(journal_name: str) -> str:
    """
    Abbreviate common journal names.
    
    Input:
        journal_name = "Journal of Bone and Joint Surgery"
    Output:
        "J Bone Joint Surg"
    
    Input:
        journal_name = "New England Journal of Medicine"
    Output:
        "N Engl J Med"
    
    Input (unknown journal - return as-is):
        journal_name = "Some Obscure Journal"
    Output:
        "Some Obscure Journal"
    """
    # TODO: Implement
    # return JOURNAL_ABBREVIATIONS.get(journal_name, journal_name)
    pass


def format_reference_list(articles: list[dict]) -> str:
    """
    Format a numbered reference list from multiple articles.
    
    Input:
        articles = [
            {"authors": ["Smith J"], "title": "First article", "journal": "JAMA", "year": 2023, "volume": "330", "pages": "45-50"},
            {"authors": ["Johnson M", "Williams K"], "title": "Second article", "journal": "Lancet", "year": 2024, "volume": "403", "pages": "112-118"}
        ]
    
    Output:
        "References
        
        1. Smith J. First article. JAMA. 2023;330:45-50.
        2. Johnson M, Williams K. Second article. Lancet. 2024;403:112-118."
    """
    # TODO: Implement
    # if not articles:
    #     return "References\n\nNo references cited."
    #
    # lines = ["References", ""]
    # for i, article in enumerate(articles, 1):
    #     citation = format_citation(article)
    #     lines.append(f"{i}. {citation}")
    #
    # return "\n".join(lines)
    pass


# Superscript number mapping for inline citations
SUPERSCRIPT_MAP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def create_inline_citation(reference_numbers: list[int]) -> str:
    """
    Create superscript inline citation markers.
    
    Input:
        reference_numbers = [1]
    Output:
        "¹"
    
    Input:
        reference_numbers = [1, 2]
    Output:
        "¹˒²"
    
    Input:
        reference_numbers = [1, 2, 3]
    Output:
        "¹⁻³"  # Range format for 3+ consecutive numbers
    
    Input:
        reference_numbers = [12]
    Output:
        "¹²"
    """
    # TODO: Implement
    # Simple version:
    # numbers_str = ",".join(str(n) for n in reference_numbers)
    # return numbers_str.translate(SUPERSCRIPT_MAP)
    pass


def add_citations_to_text(text: str, citation_positions: list[dict]) -> str:
    """
    Add inline citation markers to generated text.
    
    Input:
        text = "Pain management typically includes acetaminophen. Ice therapy is recommended for swelling. Rest is important for recovery."
        citation_positions = [
            {"after_phrase": "acetaminophen", "reference_numbers": [1]},
            {"after_phrase": "swelling", "reference_numbers": [2, 3]}
        ]
    
    Output:
        "Pain management typically includes acetaminophen.¹ Ice therapy is recommended for swelling.²˒³ Rest is important for recovery."
    
    Implementation approach:
        1. Sort citations by position in text (end to beginning to preserve indices)
        2. For each citation, find the phrase and insert superscript after it
        3. Return modified text
    """
    # TODO: Implement
    # Process in reverse order so indices don't shift
    # sorted_citations = sorted(citation_positions, key=lambda c: text.find(c["after_phrase"]), reverse=True)
    #
    # for citation in sorted_citations:
    #     phrase = citation["after_phrase"]
    #     ref_nums = citation["reference_numbers"]
    #     superscript = create_inline_citation(ref_nums)
    #     
    #     # Find phrase and insert superscript after it
    #     pos = text.find(phrase)
    #     if pos != -1:
    #         insert_pos = pos + len(phrase)
    #         text = text[:insert_pos] + superscript + text[insert_pos:]
    #
    # return text
    pass


# Test the module
if __name__ == "__main__":
    # Example usage - uncomment to test:
    #
    # # Test single citation
    # article1 = {
    #     "authors": ["Smith JA", "Johnson MB"],
    #     "title": "Outcomes in total knee arthroplasty",
    #     "journal": "Journal of Bone and Joint Surgery",
    #     "year": 2023,
    #     "volume": "105",
    #     "issue": "3",
    #     "pages": "234-241"
    # }
    # print("Single citation:")
    # print(format_citation(article1))
    # # Expected: Smith JA, Johnson MB. Outcomes in total knee arthroplasty. J Bone Joint Surg. 2023;105(3):234-241.
    #
    # # Test many authors (et al.)
    # article2 = {
    #     "authors": ["Smith J", "Johnson M", "Williams K", "Brown R", "Davis T", "Wilson P", "Taylor M"],
    #     "title": "Large multicenter trial",
    #     "journal": "New England Journal of Medicine",
    #     "year": 2024,
    #     "volume": "390",
    #     "pages": "112-125"
    # }
    # print("\nMany authors (et al.):")
    # print(format_citation(article2))
    # # Expected: Smith J, Johnson M, Williams K, et al. Large multicenter trial. N Engl J Med. 2024;390:112-125.
    #
    # # Test reference list
    # print("\nReference list:")
    # print(format_reference_list([article1, article2]))
    #
    # # Test inline citations
    # text = "Pain medication helps recovery. Ice reduces swelling."
    # citations = [
    #     {"after_phrase": "recovery", "reference_numbers": [1]},
    #     {"after_phrase": "swelling", "reference_numbers": [2]}
    # ]
    # print("\nWith inline citations:")
    # print(add_citations_to_text(text, citations))
    # # Expected: Pain medication helps recovery.¹ Ice reduces swelling.²
    pass