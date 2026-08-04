from project import read_genes_from_file, find_matches, display_results

def test_read_genes_from_file():
    with open("genes.txt", "w") as f:
        f.write("GeneA: ATCG\n")
        f.write("GeneB: GGTT\n")
    assert read_genes_from_file() == {"GeneA":"ATCG", "GeneB":"GGTT"}

def test_read_genes_from_file_lowercase():
    with open("genes.txt", "w") as f:
        f.write("GeneA: atcg\n")
    assert read_genes_from_file() == {"GeneA":"ATCG"}

def test_read_genes_from_file_extra_spaces():
    with open("genes.txt", "w") as f:
        f.write("   GeneA   :    ATCG    \n")
    assert read_genes_from_file() == {"GeneA":"ATCG"}

def test_find_matches_exact_match():
    genes = {"BRCA1":"CGCTGCTCCCTCTTTGCGAGAACTGCACTT", "TP53":"TCATACAGCCCCAAGCACGGCCCATGGGAT"}
    matches = find_matches(genes, "CGCTGCTCCCTCTTTGCGAGAACTGCACTT")
    assert ("BRCA1", 100.0) in matches
    assert len(matches) == 1

def test_find_matches_no_match():
    genes = {"GeneA":"AAAAAA"}
    assert find_matches(genes, "GGGGGG") == []

def test_find_matches_lowercase_input():
    genes = {"GeneA":"ATCGATCG"}
    assert find_matches(genes, "atcgatcg") == [("GeneA", 100.0)]

def test_find_matches_multiple_matches():
    genes = {"GeneA":"ATCGATCG", "GeneB":"ATCGATCG", "GeneC":"GGGGGGGG"}
    matches = find_matches(genes, "ATCGATCG")
    assert len(matches) == 2
    assert ("GeneA", 100.0) in matches
    assert ("GeneB", 100.0) in matches

def test_find_matches_empty_dictionary():
    assert find_matches({}, "ATCG") == []

def test_find_matches_high_threshold():
    genes = {"GeneA":"ATCGATCG"}
    matches = find_matches(genes, "ATCGATCA", threshold=1.0)
    assert matches == []

def test_find_matches_real_gene():
    genes = {"CFTR":"AGTATAAGGTATTGCGATAGACCGTAACGT"}
    matches = find_matches(genes, "AGTATAAGGTATTGCGATAGACCGTAACGT")
    assert matches == [("CFTR", 100.0)]

def test_display_results_no_matches():
    assert display_results([]) == "No matching genes found."

def test_display_results_single_match():
    result = display_results([("GeneX", 95.0)])
    assert result == (
        "Matching genes found:\n"
        "GeneX (95.0%)"
    )

def test_display_results_multiple_matches():
    result = display_results([("GeneA", 100.0), ("GeneB", 91.5)])
    expected = (
        "Matching genes found:\n"
        "GeneA (100.0%)\n"
        "GeneB (91.5%)"
    )
    assert result == expected

def test_display_results_three_matches():
    result = display_results([
        ("GeneA", 100.0),
        ("GeneB", 97.5),
        ("GeneC", 92.1)
    ])
    expected = (
        "Matching genes found:\n"
        "GeneA (100.0%)\n"
        "GeneB (97.5%)\n"
        "GeneC (92.1%)"
    )
    assert result == expected

def test_find_matches_exact_threshold():
    genes = {"GeneA": "ATCGATCG"}
    matches = find_matches(genes, "ATCGATCG", threshold=1.0)
    assert matches == [("GeneA", 100.0)]
