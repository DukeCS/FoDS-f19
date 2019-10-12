test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The table should have 31 rows
          >>> pivot_table.num_rows
          31
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The table should be the same as the one in the csv
          >>> x = Table().read_table('tests/q6_result.csv')
          >>> tables_are_same(x, pivot_table)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
