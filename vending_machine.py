POP_VENDING_MACHINE = {
'Cool Cola': 3.59,
'Mighty Mist': 4.27,
'Butter Beer': 5.99
}


def vend_pop(pop_selection, money_amount_paid):
  """
  Vends pop given a str name of the pop and sufficient money.
  Return the change, if overpaid.
  """
  amount_paid = float(money_amount_paid)

  if amount_paid <= 0:
    raise ValueError('Please insert coins. No freebies!')

  if not pop_selection in POP_VENDING_MACHINE:
    raise ValueError('Invalid selection: {}'.format(pop_selection))

  cost = POP_VENDING_MACHINE[pop_selection]
  print "Here's some pop: {}".format(pop_selection)

  if amount_paid < cost:
    raise ValueError('Not enough coins. Insert {} more!'.format(cost - amount_paid))

  return amount_paid - cost
