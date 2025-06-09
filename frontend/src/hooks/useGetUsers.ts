import { useQuery } from '@tanstack/react-query'
import type { UserList } from '../types/user'
import config from '../config'

export const useGetUsers = () => {
  return useQuery<UserList, Error>({
    queryKey: ['userList'],
    queryFn: async () => {
      const response = await fetch(`${config.backend_url}/users`)
      return await response.json()
    },
  })
}
