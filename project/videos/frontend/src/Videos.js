import React, {Component} from "react";
import VideoService from "./VideoService";

const videoService = new VideoService();

export default class Videos extends Component {
constructor(props){
    super(props)
    this.state = {
        data : [],
        inputValue: ''
    }

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
}
getData(){
    videoService.getVideos().then(result => {
        this.setState({data: result.data})
    	})
}

componentDidMount(){
    this.getData()
}
setLike(video) {
    videoService.setLikeVideo(video.id)
    video.likesCount += 1
    this.forceUpdate()
}
render() {
    return (
        <div id = 'videos'>
        {this.state.data.map(video =>
            <div id = {'video_' + video.id}>
                <p> {video.text} </p>
                <button onClick={() => this.setLike(video)}>  {video.likesCount}</button>
                <p> Date : {video.date}</p>
                <hr/>
            </div>
        )}
        <input type='text' onChange={this.handleChange} value={this.state.inputValue}></input><button onClick={this.handleSubmit}>Send</button>
        </div>
    	)
}
}