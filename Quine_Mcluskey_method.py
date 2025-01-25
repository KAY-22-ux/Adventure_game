def bin_representation():
    minterms = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
    dont_cares = [4, 15]
    
    minterms_bin = [bin(minterm)[2:].zfill(4) for minterm in minterms]
    dont_cares_bin = [bin(dc)[2:].zfill(4) for dc in dont_cares]
    
    minterms_bin = list(set(minterms_bin) - set(dont_cares_bin))  # Remove don't-care terms from minterms
    return minterms_bin

# Function to group minterms based on number of 1's in their binary representation
def group_minterms():
    minterms_bin = bin_representation()
    groups = {0: [], 1: [], 2: [], 3: []}
    
    for term in minterms_bin:
        ones_count = sum(1 for bit in term if bit == '1')
        groups[ones_count].append(term)
    return groups

# Function to combine two terms if they differ by only one bit
def combine_terms(term1, term2):
    diff_count = sum(1 for i in range(len(term1)) if term1[i] != term2[i])
    if diff_count == 1:
        combined = ''.join(term1[i] if term1[i] == term2[i] else '-' for i in range(len(term1)))
        return combined
    return None

# Quine-McCluskey minimization method
def quine_mccluskey():
    groups = group_minterms()
    
    # Step 1: Combine terms
    combined_terms = []
    for i in range(3):
        group1 = groups[i]
        group2 = groups[i+1]
        for term1 in group1:
            for term2 in group2:
                combined = combine_terms(term1, term2)
                if combined:
                    combined_terms.append(combined)
    
    # Step 2: Identify prime implicants
    prime_implicants = list(set(combined_terms))
    essential_implicants = []  # This would be determined based on coverage of min
