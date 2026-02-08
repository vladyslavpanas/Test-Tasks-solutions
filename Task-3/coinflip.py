# Задані ймовірності випадіння 'H' для 4 монет
coin_probs = [0.12, 0.27, 0.21, 0.96]
# Початкові шанси для кожної монети
priors = [0.25, 0.25, 0.25, 0.25]
# Послідовність результатів тестів
observations = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'H']
results = []
print("Покроковий розрахунок:")
for obs in observations:
    # Теорема Байєса
    unnormalized_posteriors = []
    for i in range(4):
        # Якщо випав 'H', беремо ймовірність монети P(H), якщо 'T' — то 1 - P(H)
        likelihood = coin_probs[i] if obs == 'H' else (1 - coin_probs[i])
        # Чисельник Байєса: P(Data|Coin) * P(Coin)
        unnormalized_posteriors.append(likelihood * priors[i])
    # Сума для нормалізації (знаменник Байєса)
    total_prob = sum(unnormalized_posteriors)
    # Нормалізування, щоб сума ймовірностей знову дорівнювала 1
    priors = [p / total_prob for p in unnormalized_posteriors]
    # Передбачення наступного кидка
    # Сума (ймовірність монети * поточна віра в цю монету)
    next_flip_prob_h = sum(priors[i] * coin_probs[i] for i in range(4))
    # Додавання результату, округленого до сотих
    results.append(round(next_flip_prob_h, 2))
    print("Після '{}': ймовірність наступного 'H' = {:.4f} -> {}".format(obs, next_flip_prob_h, results[-1]))
print("\nФінальний список (як у завданні):")
print(results)