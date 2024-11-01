FROM node:18.19.0 AS build-deps

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . ./

RUN yarn build

FROM nginx:1.27.2-alpine

COPY --from=build-deps /app/build /usr/share/nginx/html

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
