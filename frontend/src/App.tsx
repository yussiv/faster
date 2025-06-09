import type React from 'react'
import AddUser from './components/AddUser'
import { useDeleteUser } from './hooks/useDeleteUser'
import { useGetUsers } from './hooks/useGetUsers'
import { useQueryClient } from '@tanstack/react-query'

function App() {
  const { isPending, error, data: users, isFetching } = useGetUsers()
  const { mutate: deleteUser, isError } = useDeleteUser()
  const queryClient = useQueryClient()

  const handleDelete = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault()
    deleteUser(e.currentTarget.value, {
      onSuccess: () => {
        queryClient.invalidateQueries({ queryKey: ['userList'] })
      },
    })
  }

  if (isPending) {
    return <div>Loading...</div>
  }

  if (error) {
    console.log(error)
    return <div>Failed to load user list</div>
  }

  return (
    <>
      <h1>Users</h1>
      {isError && <div className="error">Delete failed</div>}
      <div>
        <ul>
          {users.users.map((user) => (
            <li>
              <span>{user.username}</span>
              <button className="delete" onClick={handleDelete} value={user.id}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      </div>
      <div>{isFetching ? 'Updating...' : ''}</div>
      <AddUser />
    </>
  )
}

export default App
