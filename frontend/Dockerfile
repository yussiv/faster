FROM node:24-bookworm-slim

USER node
WORKDIR /app

COPY package.json tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts index.html ./

RUN npm install

COPY public ./public
COPY src ./src

EXPOSE 5173

CMD [ "npm", "run", "dev", "--", "--host" ]