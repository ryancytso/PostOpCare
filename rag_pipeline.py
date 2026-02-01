# rag_pipeline.py
"""
RAG Pipeline for PostopCare

This module combines all components into a working RAG system:
    1. Vector Store (vector_store.py) - retrieval
    2. LLM Client (llm_client.py) - generation
    3. Prompt Manager (prompt_manager.py) - templates
    4. Citation Formatter (citation_formatter.py) - citations

Setup:
    Ensure these modules are complete and working:
    - vector_store.py (Ticket 5)
    - llm_client.py (Ticket 2)
    - prompt_manager.py (Ticket 3)
    - citation_formatter.py (Ticket 8)
    
    And that Pinecone index has been populated with medical literature (Ticket 1 + 4 + 5)
"""

import logging
from typing import Optional
from datetime import datetime

# Import our modules
from vector_store import search as vector_search
from llm_client import generate_with_context
from prompt_manager import PromptManager
from citation_formatter import format_reference_list

# Set up logging - this helps us debug the pipeline
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("rag_pipeline")

# Initialize prompt manager
prompt_manager = PromptManager()


def generate_handout_section(
    procedure: str,
    section: str,
    top_k: int = 5
) -> dict:
    """
    Generate a single handout section using RAG.
    
    Pipeline Steps:
        1. Build search query from procedure + section
        2. Retrieve relevant chunks from vector store
        3. Format context from retrieved chunks
        4. Load prompt template for section type
        5. Call LLM with context + prompt
        6. Return generated content with sources
    
    Input:
        procedure = "knee replacement"
        section = "pain_management"
        top_k = 5
    
    Output:
        {
            "procedure": "knee replacement",
            "section": "pain_management",
            "content": "## Pain Management After Knee Replacement\n\nSome pain and discomfort after surgery is normal and expected. Your pain should gradually improve each day.\n\n**Medications:**\n- Take your prescribed pain medication as directed by your surgeon\n- You may use over-the-counter acetaminophen (Tylenol) between doses\n- Avoid ibuprofen and aspirin for the first 2 weeks unless approved by your doctor\n\n**Ice Therapy:**\n- Apply ice packs for 20 minutes at a time, several times a day\n- Use a thin towel between ice and skin to prevent ice burn\n- Ice is most effective in the first 2 weeks after surgery\n\n**When to Call Your Doctor:**\n- Pain suddenly gets much worse\n- Pain medication is not helping at all\n- You have severe pain that rest does not improve",
            "sources": [
                {
                    "id": "pmid_12345_chunk_0",
                    "text": "Studies show acetaminophen is effective for post-surgical pain management...",
                    "score": 0.89,
                    "metadata": {"pmid": "12345", "section": "pain"}
                },
                {
                    "id": "pmid_67890_chunk_2",
                    "text": "Ice therapy applied for 20 minutes reduces inflammation...",
                    "score": 0.85,
                    "metadata": {"pmid": "67890", "section": "recovery"}
                }
            ],
            "metadata": {
                "chunks_retrieved": 5,
                "chunks_used": 5,
                "model": "gpt-4o-mini",
                "generated_at": "2025-01-15T10:30:00Z"
            }
        }
    """
    logger.info(f"=== Generating '{section}' section for '{procedure}' ===")
    
    # Step 1: Build search query
    search_query = f"{procedure} {section.replace('_', ' ')} post operative care instructions"
    logger.info(f"Step 1 - Search query: '{search_query}'")
    
    # Step 2: Retrieve relevant chunks from vector store
    # TODO: Implement
    # retrieved_chunks = vector_search(search_query, top_k=top_k)
    # logger.info(f"Step 2 - Retrieved {len(retrieved_chunks)} chunks from vector store")
    # for i, chunk in enumerate(retrieved_chunks):
    #     logger.debug(f"  Chunk {i+1} (score={chunk['score']:.3f}): {chunk['text'][:50]}...")
    
    # Step 3: Format context from retrieved chunks
    # TODO: Implement
    # context_parts = []
    # for i, chunk in enumerate(retrieved_chunks):
    #     source_info = f"[Source {i+1}: PMID {chunk['metadata'].get('pmid', 'unknown')}]"
    #     context_parts.append(f"{source_info}\n{chunk['text']}")
    # context = "\n\n".join(context_parts)
    # logger.info(f"Step 3 - Formatted context ({len(context)} characters)")
    
    # Step 4: Load prompt template
    # TODO: Implement
    # prompt = prompt_manager.get_prompt(
    #     section,
    #     procedure_name=procedure,
    #     context=context
    # )
    # logger.info(f"Step 4 - Loaded prompt template '{section}'")
    
    # Step 5: Call LLM with context
    # TODO: Implement
    # logger.info("Step 5 - Calling LLM...")
    # content = generate_with_context(
    #     prompt=f"Write {section.replace('_', ' ')} instructions for {procedure}",
    #     context=context,
    #     system_prompt="You are a medical writer creating patient-friendly post-operative instructions. Write at a 6th-8th grade reading level. Be specific and actionable."
    # )
    # logger.info(f"Step 5 - Generated {len(content)} characters")
    
    # Step 6: Return result
    # TODO: Implement
    # result = {
    #     "procedure": procedure,
    #     "section": section,
    #     "content": content,
    #     "sources": retrieved_chunks,
    #     "metadata": {
    #         "chunks_retrieved": len(retrieved_chunks),
    #         "model": "gpt-4o-mini",
    #         "generated_at": datetime.now().isoformat()
    #     }
    # }
    # logger.info(f"=== Completed '{section}' section ===\n")
    # return result
    
    pass


def generate_full_handout(procedure: str, sections: Optional[list[str]] = None) -> dict:
    """
    Generate a complete handout with all sections.
    
    Input:
        procedure = "appendectomy"
        sections = None  # Uses default sections
    
    Output:
        {
            "procedure": "appendectomy",
            "title": "After Your Appendectomy: Recovery Guide",
            "generated_at": "2025-01-15T10:30:00Z",
            "sections": [
                {
                    "name": "Overview",
                    "content": "You have just had an appendectomy..."
                },
                {
                    "name": "Pain Management",
                    "content": "Some discomfort after surgery is normal..."
                },
                {
                    "name": "Activity Restrictions",
                    "content": "For the first 1-2 weeks, avoid lifting..."
                },
                {
                    "name": "Wound Care",
                    "content": "Keep your incision clean and dry..."
                },
                {
                    "name": "Warning Signs",
                    "content": "Call your doctor immediately if..."
                },
                {
                    "name": "Follow-Up",
                    "content": "Your follow-up appointment is scheduled..."
                }
            ],
            "all_sources": [...],
            "quality_metrics": {
                "total_sections": 6,
                "total_sources_used": 25,
                "generation_time_seconds": 45.2
            }
        }
    """
    import time
    start_time = time.time()
    
    # Default sections for a complete handout
    if sections is None:
        sections = [
            "overview",
            "pain_management",
            "activity_restrictions",
            "wound_care",
            "warning_signs",
            "follow_up"
        ]
    
    logger.info(f"Generating full handout for '{procedure}' with {len(sections)} sections")
    
    # TODO: Implement
    # generated_sections = []
    # all_sources = []
    #
    # for section in sections:
    #     logger.info(f"Generating section: {section}")
    #     result = generate_handout_section(procedure, section)
    #     
    #     generated_sections.append({
    #         "name": section.replace("_", " ").title(),
    #         "content": result["content"]
    #     })
    #     all_sources.extend(result["sources"])
    #
    # elapsed_time = time.time() - start_time
    # logger.info(f"Full handout generated in {elapsed_time:.1f} seconds")
    #
    # return {
    #     "procedure": procedure,
    #     "title": f"After Your {procedure.replace('_', ' ').title()}: Recovery Guide",
    #     "generated_at": datetime.now().isoformat(),
    #     "sections": generated_sections,
    #     "all_sources": all_sources,
    #     "quality_metrics": {
    #         "total_sections": len(generated_sections),
    #         "total_sources_used": len(all_sources),
    #         "generation_time_seconds": round(elapsed_time, 1)
    #     }
    # }
    
    pass


# Test the module
if __name__ == "__main__":
    # Example usage - uncomment to test:
    #
    # # Test 1: Generate single section for knee replacement
    # print("=" * 60)
    # print("TEST 1: Single section - Knee Replacement Pain Management")
    # print("=" * 60)
    # result = generate_handout_section("knee replacement", "pain_management")
    # print(f"\nGenerated content:\n{result['content']}")
    # print(f"\nSources used: {len(result['sources'])}")
    #
    # # Test 2: Generate single section for appendectomy
    # print("\n" + "=" * 60)
    # print("TEST 2: Single section - Appendectomy Activity Restrictions")
    # print("=" * 60)
    # result = generate_handout_section("appendectomy", "activity_restrictions")
    # print(f"\nGenerated content:\n{result['content']}")
    #
    # # Test 3: Generate full handout
    # print("\n" + "=" * 60)
    # print("TEST 3: Full handout - Knee Replacement")
    # print("=" * 60)
    # handout = generate_full_handout("knee replacement")
    # print(f"\nTitle: {handout['title']}")
    # print(f"Sections generated: {handout['quality_metrics']['total_sections']}")
    # print(f"Total sources: {handout['quality_metrics']['total_sources_used']}")
    # print(f"Time: {handout['quality_metrics']['generation_time_seconds']}s")
    # 
    # for section in handout['sections']:
    #     print(f"\n--- {section['name']} ---")
    #     print(section['content'][:200] + "...")
    pass