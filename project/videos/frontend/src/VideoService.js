import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class VideoService{

    constructor(){}


    getVideos() {
    const url = `${API_URL}/api/videos/`;
    return axios.get(url).then(response => response.data);
    }

    setLikeVideo(id) {
    const url = `${API_URL}/api/like_video/` + id;
    return axios.get(url).then(response => response.data);
    }

}