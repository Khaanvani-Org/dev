graph TD
  subgraph Dev
    A((Develop Code))
    B((Code Review))
    C((Merge Changes))
  end

  subgraph Test
    D((Deploy to Test Environment))
    E((Run Tests))
    F((Review Results))
  end

  subgraph Prod
    G((Deploy to Production Environment))
    H((Monitor Performance))
    I((Handle Issues))
  end

  A -->|Code Review Passed| C
  C -->|Deploy to Test| D
  D -->|Tests Passed| E
  E -->|Review Passed| F
  F -->|Deploy to Prod| G
  G -->|Healthy| H
  H -->|Issues Occur| I
  I -->|Resolved| A
