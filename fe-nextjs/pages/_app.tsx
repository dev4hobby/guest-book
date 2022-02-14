import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Head from 'next/head'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Guest Book</title>
        <meta charSet="UTF-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        {/* 여기 공유할 때 사용할 메타정보 넣어줘.. (이미지랑 텍스트) */}
      </Head>
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
