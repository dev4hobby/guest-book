export interface IComment {
  comments: CommentObject[]
}

export interface CommentObject {
  id: {
    oid: string
  },
  content: string,
  publishe_date: {
    date: string
  }
}