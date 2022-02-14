import fetch from 'cross-fetch'

export interface FetchResult<T> {
  status: number
  body: T
}

export const fetcher = async <T>(url: string): Promise<FetchResult<T>> => {
  const response = await fetch(url)
  const body = await response.json()
  return {
    status: response.status,
    body,
  }
}