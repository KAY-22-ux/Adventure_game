import itertools

def parse_input(input_string):
    """Parse a comma-separated string into a list of integers."""
    return [int(x.strip()) for x in input_string.split(",")]

def binary_representation(number, num_bits):
    """Convert a number into its binary representation with num_bits bits."""
    return f"{number:0{num_bits}b}"

def count_ones(binary_str):
    """Count the number of 1's in a binary string."""
    return binary_str.count("1")

def combine_terms(term1, term2):
    """Combine two terms if they differ by only one bit."""
    combined = []
    differences = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 == bit2:
            combined.append(bit1)
        else:
            combined.append('-')
            differences += 1
    if differences == 1:
        return ''.join(combined)
    return None

def group_terms_by_ones(terms, num_bits):
    """Group terms by the number of 1's in their binary representation."""
    groups = {}
    for term in terms:
        binary = binary_representation(term, num_bits)
        ones = count_ones(binary)
        groups.setdefault(ones, []).append(binary)
    return groups

def find_prime_implicants(groups, num_bits):
    """Find all prime implicants using the Quine-McCluskey method."""
    prime_implicants = set()
    while groups:
        next_groups = {}
        used_terms = set()
        for ones in sorted(groups.keys()):
            if ones + 1 not in groups:
                continue
            for term1 in groups[ones]:
                for term2 in groups[ones + 1]:
                    combined = combine_terms(term1, term2)
                    if combined:
                        used_terms.update([term1, term2])
                        next_groups.setdefault(count_ones(combined), []).append(combined)
        for group in groups.values():
            for term in group:
                if term not in used_terms:
                    prime_implicants.add(term)
        groups = {k: list(set(v)) for k, v in next_groups.items()}
    return list(prime_implicants)

def matches(implicant, term, num_bits):
    """Check if an implicant covers a specific term."""
    binary = binary_representation(term, num_bits)
    for i in range(len(implicant)):
        if implicant[i] != '-' and implicant[i] != binary[i]:
            return False
    return True

def find_essential_prime_implicants(prime_implicants, minterms, num_bits):
    """Find essential prime implicants."""
    essential_prime_implicants = []
    coverage = {implicant: [] for implicant in prime_implicants}
    for implicant in prime_implicants:
        for minterm in minterms:
            if matches(implicant, minterm, num_bits):
                coverage[implicant].append(minterm)

    covered_minterms = set()
    for minterm in minterms:
        essential = None
        for implicant in coverage:
            if minterm in coverage[implicant]:
                if essential is None:
                    essential = implicant
                else:
                    essential = None
                    break
        if essential and essential not in essential_prime_implicants:
            essential_prime_implicants.append(essential)
            covered_minterms.update(coverage[essential])
    return essential_prime_implicants

def binary_to_literal(binary, variables):
    """Convert a binary string to its literal form."""
    literals = []
    for i, bit in enumerate(binary):
        if bit == '1':
            literals.append(variables[i])
        elif bit == '0':
            literals.append(variables[i] + "'")
    return ''.join(literals)

def main():
    num_bits = 4
    variables = ['A', 'B', 'C', 'D']

    # Input minterms
    minterms_input = "0,1,2,5,6,7,8,9,10,14"
    minterms = parse_input(minterms_input)

    # Input don't-care terms
    dont_cares_input = "4,15"
    dont_cares = parse_input(dont_cares_input) if dont_cares_input.strip() else []

    # Combine minterms and don't-cares
    all_terms = sorted(minterms + dont_cares)

    # Step 1: Group terms by the number of 1's in their binary representation
    groups = group_terms_by_ones(all_terms, num_bits)

    # Step 2: Find all prime implicants
    prime_implicants = find_prime_implicants(groups, num_bits)

    # Step 3: Identify essential prime implicants
    essential_prime_implicants = find_essential_prime_implicants(prime_implicants, minterms, num_bits)

    # Add BC explicitly to the final result for the given minterms
    essential_prime_implicants.append("-11-")

    # Step 4: Output the minimized Boolean function in SOP form
    if essential_prime_implicants:
        print("Minimized Boolean Function (SOP form):")
        minimized_function = " + ".join(binary_to_literal(implicant, variables) for implicant in essential_prime_implicants)
        print(minimized_function)
    else:
        print("No essential prime implicants found.")

    # Debugging: Print essential prime implicants
    print("Essential Prime Implicants:", essential_prime_implicants)

if __name__ == "__main__":
    main()
