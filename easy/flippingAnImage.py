class Solution:
    def flipAndInvertImage(self, image):
        for kit in image:
            kit.reverse()
            for i in range(len(kit)):
                if kit[i] == 1:
                    kit[i] = 0
                elif kit[i] == 0:
                    kit[i] = 1

        return image
