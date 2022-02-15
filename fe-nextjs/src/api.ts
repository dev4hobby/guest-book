export const postComment = async (): Promise<any> => {
  const message = await prompt('올해 계획을 입력해주세요..!')
  if (!message) {
    return {result: "fail"} as any
  }
  if (message && message.length < 5) {
    alert('5글자 이상 입력하세요!');
    return {result: "fail"} as any
  }
  message.replace(';','').replace('\\','')
  await fetch(`${process.env.NEXT_PUBLIC_GB_API_BASE_URL}/comments`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      content: message
    })
  })
  location.reload()
}
