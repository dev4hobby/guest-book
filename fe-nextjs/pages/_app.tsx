import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Head from 'next/head'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>담벼락: 아무말 대잔치</title>
        <meta charSet="UTF-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <meta property="og:title" content="담벼락이에요"/>
        <meta
          property="og:description"
          content="아무말이나 적어놓고 서로 공유해봅시다..!"
        />
        <meta
          property="og:image"
          content="/banner/guestbook.png"
        />
        <meta property="og:image:width" content="800" />
        <meta property="og:image:height" content="400" />
        <meta property="og:site_name" content="담벼락" />
        <meta property="og:type" content="website" />
      </Head>
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
