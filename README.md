# billing-core-demo

A tiny invoice-math module used to demo an engineering Grok Bot governed by OMEGA.

    python3 -m unittest discover -s tests -t . -v

`main` has one real bug: tax is truncated instead of rounded to the nearest cent, so
`test_tax_of_half_a_cent_or_more_rounds_up` fails. The only way into `main` is a
pull request.
