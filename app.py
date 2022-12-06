from classes import Group, Member


group1 = Group('Group1', 100, 4)
member1 = Member('Kadir', 'Male')
member2 = Member('Ahmet', 'Male')
member3 = Member('Mehmet', 'Male')
member4 = Member('Ali', 'Male')
group1.viewBalance()
member1.deposit(400)
member2.deposit(400)
member3.deposit(400)
member4.deposit(400)

# lent money to group
member1.lend(100, group1)

member2.lend(100, group1)
group1.viewBalance()

# group borrows
group1.borrow(100, member3)
group1.borrow(100, member4)
group1.viewBalance()

# test borrow too much money
group1.borrow(500, member1)