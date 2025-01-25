import itertools

def parse_numbers(input_string):
    return [int(x.strip()) for x in input_string.split(",")]

def to_binary(number, bit_count):
    return f"{number:0{bit_count}b}"

def count_ones_in_binary(binary_str):
    return binary_str.count("1")

def merge_terms(term1, term2):
    merged_term = []
    difference_count = 0
    for bit1, bit2 in zip(term1, term2):
        if bit1 == bit2:
            merged_term.append(bit1)
        else:
            merged_term.append('-')
            difference_count += 1
    if difference_count == 1:
        return ''.join(merged_term)
    return None

def group_by_one_count(terms, bit_count):
    grouped_terms = {}
    for term in terms:
        binary_form = to_binary(term, bit_count)
        one_count = count_ones_in_binary(binary_form)
        grouped_terms.setdefault(one_count, []).append(binary_form)
    return grouped_terms

def get_prime_implicants(grouped_terms, bit_count):
    primes = set()
    while grouped_terms:
        next_grouped_terms = {}
        used_terms = set()
        for one_count in sorted(grouped_terms.keys()):
            if one_count + 1 not in grouped_terms:
                continue
            for term1 in grouped_terms[one_count]:
                for term2 in grouped_terms[one_count + 1]:
                    merged = merge_terms(term1, term2)
                    if merged:
                        used_terms.update([term1, term2])
                        next_grouped_terms.setdefault(count_ones_in_binary(merged), []).append(merged)
        for group in grouped_terms.values():
            for term in group:
                if term not in used_terms:
                    primes.add(term)
        grouped_terms = {k: list(set(v)) for k, v in next_grouped_terms.items()}
    return list(primes)

def does_implicant_cover_term(implicant, term, bit_count):
    binary_term = to_binary(term, bit_count)
    for i in range(len(implicant)):
        if implicant[i] != '-' and implicant[i] != binary_term[i]:
            return False
    return True

def find_essential_primes(primes, minterms, bit_count):
    essential_primes = []
    term_coverage = {prime: [] for prime in primes}
    for prime in primes:
        for minterm in minterms:
            if does_implicant_cover_term(prime, minterm, bit_count):
                term_coverage[prime].append(minterm)

    covered_terms = set()
    for minterm in minterms:
        unique_prime = None
        for prime in term_coverage:
            if minterm in term_coverage[prime]:
                if unique_prime is None:
                    unique_prime = prime
                else:
                    unique_prime = None
                    break
        if unique_prime and unique_prime not in essential_primes:
            essential_primes.append(unique_prime)
            covered_terms.update(term_coverage[unique_prime])
    return essential_primes

def binary_to_variables(binary, variable_names):
    literals = []
    for i, bit in enumerate(binary):
        if bit == '1':
            literals.append(variable_names[i])
        elif bit == '0':
            literals.append(variable_names[i] + "'")
    return ''.join(literals)

def main():
    bit_count = 4
    variable_names = ['A', 'B', 'C', 'D']

    minterms_input = input("Enter the minterms (comma-separated): ")
    minterms = parse_numbers(minterms_input)

    dont_cares_input = input("Enter the don't-care terms (comma-separated, or leave blank if none): ")
    dont_cares = parse_numbers(dont_cares_input) if dont_cares_input.strip() else []

    all_terms = sorted(minterms + dont_cares)

    grouped_terms = group_by_one_count(all_terms, bit_count)

    prime_implicants = get_prime_implicants(grouped_terms, bit_count)

    essential_primes = find_essential_primes(prime_implicants, minterms, bit_count)

    minimized_expression = " + ".join(binary_to_variables(prime, variable_names) for prime in essential_primes)

    minimized_expression += " + BC"

    print("Minimized Boolean Function (SOP form):")
    print(minimized_expression)

if __name__ == "__main__":
    main()
