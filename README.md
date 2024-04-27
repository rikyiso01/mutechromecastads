# Mute Chromecast ADS

Mute your chromecast device when an advertisement plays

When you live with other stupid people that don't want to pay for spotify premium,
you are forced to listen to the maximum volume ads of those that are using your chromecast
device. Since I am not listening Spotify's low quality music, I don't want to be annoyed by a
moron screaming about how his podcasts are beautiful

This program will mute your chromecast when the ads are playing and will restore the original audio after it

## Usage

### pipx

> ```bash
> CHROMECAST_HOST=hostname pipx run mutechromecastads
> ```
>
> where hostname is the hostname or the ip of the chromecast device

### podman

> ```bash
> podman run --rm --env CHROMECAST_HOST=hostname ghcr.io/rikyiso01/mutechromecastads
> ```
>
> where hostname is the hostname or the ip of the chromecast device

After doing this the program will start looping and will mute the device when the broadcasted song title is 'Advertisement'
