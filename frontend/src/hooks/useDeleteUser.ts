import { useMutation } from '@tanstack/react-query'

import config from '../config'

export const useDeleteUser = () => {
  return useMutation<boolean, Error, string>({
    mutationFn: async (id: string) => {
      await fetch(`${config.backend_url}/users/${id}`, {
        method: 'DELETE',
      })
      return true
    },
  })
}
