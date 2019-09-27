init python:
    class DynamicAnimation(renpy.display.layout.DynamicDisplayable):
        """
        A dynamic image that animates through found frames
        @args:
            image_prefix: string (including folders) prefix
        @kwargs:
            image_frame_duration: float seconds
                default 0.02 (50fps)
            image_repeat: bool repeat anim
                default True
            image_bounce: bool bounce => 1,2,3,4, 3,2,1, 2,3,4
                default False
        """
        def __init__(self, *args, **kwargs):
            self.frame_duration = kwargs.get('image_frame_duration', 0.02)
            self.reverse_rotation = kwargs.get('reverse_rotation',False)
            self.repeat = kwargs.get('image_repeat', True)
            self.bounce = kwargs.get('image_bounce', False)
            self.pause, self.st_offset, self.previous_st = False, 0.0, 0.0
            self.used_images = sorted( [
                k for k in renpy.list_files()
                if k.startswith( args[0] )
                and any( [k.endswith(j) for j in ['webp']] ) ],reverse=self.reverse_rotation )

            self.num_frames = len(self.used_images)

            kwargs.update( {
                '_predict_function' : self.predict_images } )

            super(DynamicAnimation, self).__init__( self.get_frame_image,
                                                *args,
                                                **kwargs )

        def get_frame_image(self, st, at, *args, **kwargs):
            # Return image to use for this time
            if self.pause:
                self.st_offset += st - self.previous_st
            self.previous_st = st
            st -= self.st_offset
            frame = int( round( st / self.frame_duration ) )
            next_show = 0

            if not self.repeat:
                if frame >= self.num_frames:
                    frame = -1
                    next_show = None
            elif frame >= self.num_frames:
                if self.bounce and frame // self.num_frames % 2:
                    frame = self.num_frames - 1 - frame % self.num_frames
                else:
                    frame = frame % self.num_frames

            return self.used_images[frame], next_show

        def predict_images(self):
            return self.used_images