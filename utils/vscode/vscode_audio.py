import IPython.display
import numpy as np
import json

def Audio(audio: np.ndarray, rate: int):
    """
    Use instead of IPython.display.Audio as a workaround for VS Code.
    `audio` is an array with shape (channels, samples) or just (samples,) for mono.
    """

    if np.ndim(audio) == 1:
        channels = [audio.tolist()]
    else:
        channels = audio.tolist()

    return IPython.display.HTML(
        """
        <script>
    var source;
    if (!window.audioContext) {
        window.audioContext = new AudioContext();
        window.playAudio = function(audioChannels, sr) {
            const buffer = audioContext.createBuffer(audioChannels.length, audioChannels[0].length, sr);
            for (let [channel, data] of audioChannels.entries()) {
                buffer.copyToChannel(Float32Array.from(data), channel);
            }
    
            source = audioContext.createBufferSource();
            source.buffer = buffer;
            source.connect(audioContext.destination);
        }
        window.audioContext({json.dumps(channels)}, {rate})
    }
    window.change_view = function(){
        but = document.getElementById("ply");
        if (but.innerHTML == ">"){
            source.start();
        }
        else {
            source.suspend();
        }
        but.innerHTML = but.innerHTML == "||" ? ">":"||";
    }
</script>
<button id="ply" onclick="change_view()">></button>
<progress value="0", max="3"></progress>
<input type="range">
<select title="rate">
    <option value="8000">8000</option>
    <option value="8000">11025</option>
    <option value="8000">22050</option>
    <option value="8000">44100</option>
    <option value="8000">48000</option>
</select>hz
<button>Download</button>
        """
        
        
        
    #     """
    #     <script>
    #         if (!window.audioContext) {
    #             window.audioContext = new AudioContext();
    #             window.playAudio = function(audioChannels, sr) {
    #                 const buffer = audioContext.createBuffer(audioChannels.length, audioChannels[0].length, sr);
    #                 for (let [channel, data] of audioChannels.entries()) {
    #                     buffer.copyToChannel(Float32Array.from(data), channel);
    #                 }
            
    #                 const source = audioContext.createBufferSource();
    #                 source.buffer = buffer;
    #                 source.connect(audioContext.destination);
    #                 source.start();
    #             }
    #         }
    #     </script>
    #     <button onclick="playAudio(%s, %s)">Play</button>
    # """ % (json.dumps(channels), rate))