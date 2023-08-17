def main():
    num_people = int(input("Digite o número de pessoas: "))
    
    names = []
    heights = []
    
    for i in range(num_people):
        name = input(f"Digite o nome da pessoa {i+1}: ")
        height = float(input(f"Digite a altura da pessoa {i+1} em centímetros: "))
        
        names.append(name)
        heights.append(height)
    
    tallest_index = heights.index(max(heights))
    shortest_index = heights.index(min(heights))
    
    print(f'A pessoa mais alta é {names[tallest_index]} com {heights[tallest_index]} cm de altura.')
    print(f'A pessoa mais baixa é {names[shortest_index]} com {heights[shortest_index]} cm de altura.')

if __name__ == "__main__":
    main()
