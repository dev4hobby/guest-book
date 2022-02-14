# Guest Book

지난 구정, 모 사이트에서 HTML 클론코딩 강좌를 무료로 풀었다.  
단순히 제공되는 HTML 파일 양식에서 API fetching 과정만 맛보기로 진행 할 수 있어보였기 때문에..  
빠르게 구현할 수 있는 방식으로 서버와 클라이언트를 둘 다 만들어보면 어떨까 싶었다.  

## Backend

Serverless 사용해서 배포했다.  
약간의 디렉터리 구조를 잡아두고 사용하면 나중에도 요긴하게 사용될듯 하다.  

- 서버는 계속 비용이 발생할 것 같으니 서버리스 아키텍처를 활용하는 방법으로 구현한다.  
  - Lambda를 개별로 관리하기엔 모양새가 예쁘지 않다.
  - Serverless 프레임워크로 AWS에 배포하거나 Cloudflare의 Worker를 사용하면 좋을 것 같다.  
    - Worker를 사용해보고싶지만 안써봐서 아직 잘 모른다
    - sls는 예전에 써봤다.
      - sls + flask 조합으로 가고, API Gateway를 붙이면 좋겠다.
      - deploy단계에서 CloudFormation으로 알아서 생성해준다.

## Frontend

Next.js 사용했다. Vercel에 배포했다.  

- 클라이언트는 단순한 Static page 하나 만들면 될 것 같다.
  - 그냥 HTML 파일 하나 만들어서 Github pages로 배포할까?
    - Gatsby를 쓸까?
      - 이 마저도 인터렉티브 웹에 대한 수요가 생길 예정이라면?
  - Next.js를 쓸까?
    - 사용해본적 있다.
      - 좀 과한 면이 있지만 React를 사용할 수 있다면 뭐..
    - 그냥 욕심 한번 부려보자.

---

퍼블리싱이 제일 귀찮은 작업인 것 같다..
자자..