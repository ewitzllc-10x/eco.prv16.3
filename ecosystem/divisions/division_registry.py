from divisions.ops_division import OpsDivision

def load_divisions(global_data):
    return {
        "ops_division": OpsDivision(global_data)
    }
