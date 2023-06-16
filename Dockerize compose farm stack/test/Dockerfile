# Base image
FROM node:18.14.2-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the project files
COPY . .

# Build the React app
RUN npm run build

# Expose the container port
EXPOSE 3000

# Define the command to run the app
CMD [ "npm", "start" ]
