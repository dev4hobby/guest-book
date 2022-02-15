import type { NextPage } from 'next'
import Image from 'next/image'
import useSWR from 'swr'
import { postComment } from '../src/api'
import { getRandomInt } from '../src/utils/random'
import { fetcher } from '../src/fetcher'
import { IComment } from '../src/interfaces/api'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  const { data } = useSWR(`${process.env.NEXT_PUBLIC_GB_API_BASE_URL}/comments`, fetcher, {
    revalidateOnFocus: false,
  })
  
  if (!data) {
    return ( <div>Loading...</div> )
  } else {
    const { comments } = data.body as IComment
    let key=0
    return (
      <div className={styles.background}>
      <div className={styles.title}>
        <h1>무슨 생각 하고있나요?</h1>
        <p>담벼락에 적힌 글: <span>{comments.length}개</span></p>
        <div className={styles.btn} onClick={postComment}>벽에 낙서하기</div>
      </div>
      <div className={styles.box}>
        {comments.length === 0 ? ()=>{} : comments.map((comment) => (
          <Image
            key={key++}
            onClick={() => {alert(comment.content)}}
            src={`/images/object${getRandomInt(1, 8)}.png`}
            width={40}
            height={40}
            alt="goal"
          />
        ))}
      </div>
    </div>
    )
  }
}

export default Home
