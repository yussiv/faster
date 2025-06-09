export interface User {
  id: string
  username: string
  email: string
}

export interface UserList {
  users: User[]
}

export interface CreateUserInput {
  username: string
  password: string
  email: string
}
