import { useState, type SyntheticEvent } from 'react'
import { useCreateUser } from '../hooks/useCreateUser'
import { useQueryClient } from '@tanstack/react-query'

function AddUser() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [email, setEmail] = useState('')
  const queryClient = useQueryClient()

  const { mutate, isPending, isSuccess, isError, error } = useCreateUser()

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault()
    mutate(
      { username, password, email },
      {
        onSuccess: () => {
          queryClient.invalidateQueries({ queryKey: ['userList'] })
          setUsername('')
          setPassword('')
          setEmail('')
        },
      },
    )
  }

  return (
    <div className="card">
      <h2>Add User</h2>
      <form onSubmit={handleSubmit} name="adduser">
        <label>
          Username
          <input
            name="username"
            onChange={(e) => setUsername(e.target.value)}
            value={username}
          />
        </label>
        <label>
          Password
          <input
            name="password"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          />
        </label>
        <label>
          Email
          <input
            name="email"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
          />
        </label>
        <button type="submit" disabled={isPending}>
          Submit
        </button>
      </form>
      {isSuccess && <div className="success">User added successfully</div>}
      {isError && (
        <div className="error">
          Error occurred while submitting: <span>{error.message}</span>
        </div>
      )}
    </div>
  )
}

export default AddUser
