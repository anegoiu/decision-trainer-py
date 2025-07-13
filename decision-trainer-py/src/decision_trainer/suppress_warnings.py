"""
Comprehensive warning suppression for CrewAI project.
Import this module at the start of any script to suppress all known warnings.
"""
import warnings
import os

def suppress_all_warnings():
    """Suppress all deprecation and compatibility warnings from dependencies."""
    
    # Pydantic warnings (most specific first)
    warnings.filterwarnings("ignore", message=".*PydanticDeprecatedSince.*")
    warnings.filterwarnings("ignore", message=".*Using extra keyword arguments.*")
    warnings.filterwarnings("ignore", message=".*Accessing the.*attribute on the instance is deprecated.*")
    warnings.filterwarnings("ignore", message=".*__fields__.*deprecated.*")
    warnings.filterwarnings("ignore", message=".*__fields_set__.*deprecated.*")
    warnings.filterwarnings("ignore", message=".*model_fields.*deprecated.*")
    warnings.filterwarnings("ignore", message=".*model_computed_fields.*deprecated.*")
    
    # Module-specific deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="crewai")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="crewai_tools")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="weave")
    warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
    
    # General patterns for dependencies only
    warnings.filterwarnings("ignore", message=".*deprecated.*", category=DeprecationWarning)
    warnings.filterwarnings("ignore", message=".*is deprecated.*", category=DeprecationWarning)
    warnings.filterwarnings("ignore", message=".*will be removed.*", category=DeprecationWarning)
    
    print("🔇 Warning suppression activated")

def suppress_minimal_warnings():
    """Suppress only the most annoying warnings while keeping others visible."""
    warnings.filterwarnings("ignore", message=".*PydanticDeprecatedSince.*")
    warnings.filterwarnings("ignore", message=".*Using extra keyword arguments.*")
    warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
    print("🔕 Minimal warning suppression activated")

# Don't auto-suppress - let the user choose when to call it 