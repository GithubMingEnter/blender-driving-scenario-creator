# Changelog

## [Unreleased]

## [0.13.0] - 2022-02-08

### Added
- Helpful vertical lines to better visualize the elevation during road drawing

### Changed
- Allow exporting 4-way junctions with a missing connection to easily build
  T-junctions until the availability of better junction tooling

## [0.12.0] - 2022-07-22

### Fixed
- Creating degenerate arc road with infinite radius not possible (would throw
  divide by zero exception)

### Added
- Enable changing the heading at the road start by holding SHIFT

## [0.11.1] - 2022-06-22

### Fixed
- Missing shoulder in on-ramp cross section template
- Crashing export of Autobahn on-ramps/entries

## [0.11.0] - 2022-06-21

### Added

- Opening and closing of (new) lanes to create exit and entry lanes
- Splitting and merging of roads at the beginning or end to connect on-ramps and
  off-ramps, exported as OpenDRIVE direct juncions
- Examplary road cross section templates for building an RQ31 Autobahn exit

### Fixed
- Lane ID signs in GUI popup

## [0.10.2] - 2022-05-25

### Fixed
- OpenSCENARIO init action to let cars drive in the direction they have been
  placed when no trajectory is attached

## [0.10.1] - 2022-02-16

### Fixed
- Add polyline trajectory point headings which are now required for correct
  playback in esmini

## [0.10.0] - 2022-02-06

### Added
- Additional clothoid road operator using forward solver based on the curvature
  of the predecessor road section

### Fixed
- Avoid rendering blowup when start and end angle of clothoid roads are
  identical, notify user that no valid solution has been found
- Moving with ALT+MIDDLEMOUSE to only move on mouse button release

## [0.9.0] - 2022-01-23

### Added
- Double line road mark type "solid solid"
- Property for road mark weight (standard and bold)
- Property for road mark color (available: white and yellow)

### Fixed
- Initial pitch and roll of vehicle is adopted from road surface

## [0.8.0] - 2022-01-02

### Added
- Modifying elevation of roads using <kbd>E</kbd>(perspective) or
  <kbd>S</kbd>(sideview) key
- Trajectory operators can be used on elevated roads

### Changed
- Limit start and end endpoint to be not more than 10km apart

## [0.7.2] - 2021-11-07

### Fixed
- End point constraining of arc geometry

## [0.7.1] - 2021-10-25

### Fixed
- Remove duplicate road vertices
- Subdivide lane faces of long roads to avoid rendering issues

## [0.7.0] - 2021-10-24

### Added
- Operator for creating clothoid (Euler Spiral) roads

### Changed
- The road operators for all geometries are now unified and the mesh is sampled
  along the road coordinate system. This also means that all road operators now
  use the cross section configuration UI and support the selected cross
  sections.

## [0.6.0] - 2021-09-06

### Added
- Presets for road cross sections
- Some typical German standardized RAL and RAA road cross sections (RQ9, RQ11,
  RQ31, RQ36, RQ43.5)

### Fixed
- Export crashing when no trajectories exist

## [0.5.0] - 2021-08-30

### Added
- Operator for creating NURBS trajectories

### Fixed
- Path pointing from .xosc file to .xodr file (LogicFile path) not being written
  as relative path

## [0.4.0] - 2021-08-25

### Added
- Operator for creating polyline trajectories

### Fixed
- Icon .png files missing in previous releases now contained in repository and
  release .zip file

## [0.3.0] - 2021-08-17

### Added
- Configurable name, color and initial speed for car objects
- Export of car models with different colors

## [0.2.0] - 2021-08-08

### Added
- Option to export meshes as .fbx files
- Option to export meshes as .gltf files
- Configurable number and type of lanes for straight roads
- Configurable road mark type for straight roads (solid and broken)

## [0.1.1] - 2021-06-21

### Fixed
- Avoid exporter crash and display error message if junction is not fully
  connected

## [0.1.0] - 2021-06-11

### Added
- Operator for creating straight line roads
- Operator for creating arc roads
- Operator for creating 4-way junctions
- Road and junction snapping
- Snapping to grid with <kbd>Ctrl</kbd> modifier key
- Solid lane lines for arc and straight roads
- Operator for creating cars
- Export OpenSCENARIO and OpenDRIVE files using scenariogeneration lib
- Export meshes as .osgb files for esmini using osgconv


[Unreleased]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.13.0...HEAD
[0.13.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.11.1...v0.12.0
[0.11.1]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.10.2...v0.11.0
[0.10.2]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.10.1...v0.10.2
[0.10.1]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.10.0...v0.10.1
[0.10.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.7.2...v0.8.0
[0.7.2]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/johschmitz/blender-driving-scenario-creator/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/johschmitz/blender-driving-scenario-creator/releases/tag/v0.1.0
