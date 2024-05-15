import axios from "axios";
import { getFromStore, removeFromStore } from "../utils/util";
import { USER_TOKEN } from "../constants/storage";

const axiosInstance = axios.create();

const requestConfigInterceptor = function (config) {
  const token = getFromStore(USER_TOKEN);
  if (token) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
};

const responseConfigInterceptor = function (response) {
  console.log(response);
  return response;
};

axiosInstance.interceptors.request.use(
  requestConfigInterceptor,
  function (error) {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  responseConfigInterceptor,
  function (error) {

    if (error.response) {
        // The request was made and the server responded with a status code that falls out of the range of 2xx
      console.error("Error status:", error.response.status);
      console.error("Error data:", error.response.data);
      console.error("Error headers:", error.response.headers);
      if(error.response.status === 401){
        removeFromStore(USER_TOKEN)
        window.location.href = '/';
      }
    } else if (error.request) {
      // The request was made but no response was received
      console.error("Error request:", error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error("Error message:", error.message);
    }
    
    return Promise.reject(error);
  }
);

export default axiosInstance;
