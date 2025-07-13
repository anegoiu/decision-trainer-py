#!/usr/bin/env python3
"""
Test script to verify print statements work with warning suppression.
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_print_statements():
    """Test that print statements work properly."""
    print("✅ Starting print test...")
    print("✅ Basic print works")
    
    # Test with warning suppression
    from decision_trainer.suppress_warnings import suppress_minimal_warnings, suppress_all_warnings
    
    print("✅ Imported warning suppression modules")
    
    suppress_minimal_warnings()
    print("✅ Minimal warning suppression applied")
    
    suppress_all_warnings()  
    print("✅ Full warning suppression applied")
    
    # Test importing problematic modules
    try:
        import weave
        print("✅ Weave imported successfully")
    except Exception as e:
        print(f"❌ Error importing weave: {e}")
    
    try:
        from crewai import Agent
        print("✅ CrewAI imported successfully")
    except Exception as e:
        print(f"❌ Error importing crewai: {e}")
    
    print("✅ All print tests completed!")

if __name__ == "__main__":
    test_print_statements() 