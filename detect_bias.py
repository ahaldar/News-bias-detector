import sys
import detector_class
import logger
import bias_type.partisan
import bias_type.sensational

def bias_detector(content):
    detector = detector_class.create()
    bias_type.partisan.define_bias_types(detector)
    bias_type.sensational.define_bias_types(detector)
    return detector.detect(content)

def main():
    result = bias_detector(sys.argv[1])
    logger.report(result, {'verbose': False})

if __name__ == "__main__":
    main()
