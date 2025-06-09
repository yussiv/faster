import { useMutation } from '@tanstack/react-query'

import config from '../config'
import type { CreateUserInput, User } from '../types/user'

export const useCreateUser = () => {
  return useMutation<User, Error, CreateUserInput>({
    mutationFn: async (input: CreateUserInput) => {
      const response = await fetch(`${config.backend_url}/users`, {
        method: 'POST',
        body: JSON.stringify(input),
        headers: {
          'content-type': 'application/json',
        },
      })
      return await response.json()
    },
  })
}
