test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your estimate should be positive, and should also not be absurdly large
          >>> 0 < eth_predictor(10) < 100
          True
          >>> np.allclose(eth_predictor(np.arange(10,15)), [ 2.6421542 , 2.69252572, 2.74289723, 2.79326875, 2.84364026])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
