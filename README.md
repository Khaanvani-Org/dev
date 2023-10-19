```mermaid
flowchart TD;

A[User] -->|Changes| B(Dev)
B --> C{Bandit&Super-Linter Test Passed?}
C -->|Success| D(Test)
D -->E{Bandit,Super-Linter,Selnium,Wapiti Test Passed?} 
E -->|Success| F(Prod)

