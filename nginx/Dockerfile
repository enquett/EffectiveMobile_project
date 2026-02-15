FROM nginx:alpine 
COPY . . 
EXPOSE 80 
RUN chown -R nginx:nginx /var/cache/nginx /run
USER nginx
