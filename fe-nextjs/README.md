This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.tsx`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000](http://localhost:3000/comments). This endpoint can be edited in `pages/index.tsx`.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.

## FE setting

```bash
# Next.js with typescript
yarn create next-app --typescript

# Initialize
yarn add -D eslint \
prettier \
eslint-plugin-prettier \
eslint-config-prettier \
eslint-plugin-import \
eslint-plugin-react \
eslint-plugin-react-hooks \
@typescript-eslint/parser \
@typescript-eslint/eslint-plugin


# styled-components
yarn add styled-components @types/styled-components

# 문자열 안에 스타일 들어가는 것 처리를 위한 설치
yarn add -dev babel-plugin-styled-components

# 전역 스타일링에서 이용하기 위함 
yarn add styled-reset 
```
