test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The table should have 17 rows
          >>> clippers_players.num_rows
          17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The table should be the same as the one in the csv
          >>> x = Table().read_table('tests/q2_result.csv')
          >>> tables_are_same(x, q2_ans)
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
