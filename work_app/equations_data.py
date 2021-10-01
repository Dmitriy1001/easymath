equations = [
    {
        'name': 'Найбільший спільний дільник(НСД)',
        'slug': 'nsd',
        'description': 'найбільше натуральне число, на яке ці числа діляться без остачі',
    },
    {
        'name': 'Найменше спільне кратне(НСК)',
        'slug': 'nsk',
        'description': 'найменше натуральне число, яке є кратним обох цих чисел',
    }
]


equations_detail = {
    'nsd': (
        'Найбільший спільний дільник(НСД)',
        'lambda numbers: reduce(gcd, numbers)',
    ),
    'nsk': (
        'Найменше спільне кратне(НСК)',
        'lambda args: reduce(lambda a, b: a * b // gcd(a, b), tuple(args))',
    )
}