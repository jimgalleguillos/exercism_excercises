def to_rna(dna_strand):
    RNA_COMPLEMENT = {"G":"C","C":"G","T":"A","A":"U"}
    if not dna_strand:
        return dna_strand
    result = ""
    for nucleotides in dna_strand:
        result+= RNA_COMPLEMENT[nucleotides]
    return result