graph TD
  subgraph Dev
    A((Develop<br>Code))
    B((Code<br>Review))
    C((Merge<br>Changes))
  end
  
  subgraph Test
    D((Deploy to<br>Test Environment))
    E((Run<br>Tests))
    F((Review<br>Results))
  end
  
  subgraph Prod
    G((Deploy to<br>Production Environment))
    H((Monitor<br>Performance))
    I((Handle<br>Issues))
  end

  A -->|Code Review Passed| C
  C -->|Deploy to Test| D
  D -->|Tests Passed| E
  E -->|Review Passed| F
  F -->|Deploy to Prod| G
  G -->|Healthy| H
  H -->|Issues Occur| I
  I -->|Resolved| A
