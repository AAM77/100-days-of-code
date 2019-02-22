
=begin

  Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

  The output should be two capital letters with a dot seperating them.

  It should look like this:

  Sam Harris => S.H

  Patrick Feeney => P.F

=end


# My Solution # 1
def abbrev_name(name)
  name.split().map { |w| w[0].capitalize() }.join('.')
end
