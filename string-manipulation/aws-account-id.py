part1 = ["arn", "aws", "iam:", "123456789012", "user"]
name = ":" .join (part1)

part2 = ["", "Development", "product_1234", "*"]
name2 =  "/" .join (part2)

account_id = name + name2

print(account_id)