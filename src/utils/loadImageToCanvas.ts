import loadImage from 'blueimp-load-image';

const imageLoaderConfigs = {
  maxWidth: 224,
  maxHeight: 224,
  cover: true,
  crop: true,
  canvas: true,
  crossOrigin: 'Anonymous',
}

function renderImage(img: Event | HTMLImageElement) {
  if ((img as Event).type === 'error') {
    return
  }
  try {
    const element = document.getElementById('input-canvas') as HTMLCanvasElement;
    const ctx = element.getContext('2d');
    if(ctx) {
      ctx.drawImage(img as HTMLImageElement, 0, 0);
    }
  } catch (e) {
    console.error(e)
  }
}

export default function loadImageToCanvas(url: string) {
  if (!url) {
    return;
  }
  loadImage(url, renderImage, imageLoaderConfigs);
}